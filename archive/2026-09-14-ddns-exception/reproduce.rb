# frozen_string_literal: true

# Source-level diagnostic only: no database, HTTP requests, or project edits.
require 'open3'

revision = '014fbc78422f3660b295add7a50f35cc7acdf0c8'
source_path = 'api/lib/vpsadmin/api/lifetimes.rb'
repository = File.expand_path('../../repos/vpsadmin.git', __dir__)
source, stderr, status = Open3.capture3('git', "--git-dir=#{repository}", 'show', "#{revision}:#{source_path}")
raise stderr unless status.success?

original_guard = 'next if current_user.role == :admin'
proposed_guard = 'next if current_user&.role == :admin'
raise 'Expected exactly one guard' unless source.scan(original_guard).size == 1

class AccessDenied < StandardError; end

Actor = Struct.new(:role)
State = Struct.new(:reason)
Owner = Struct.new(:object_state, :current_object_state)

def build_action(source, source_path)
  namespace = Module.new
  namespace.module_eval('module VpsAdmin; module API; end; end')
  namespace.module_eval(source, source_path, 1)
  helpers = namespace.const_get(:VpsAdmin)::API::Lifetimes::ActionHelpers

  Class.new do
    include helpers
    attr_accessor :current_user

    def error!(message)
      raise AccessDenied, message
    end
  end.new
end

def result(action, actor, *owners)
  action.current_user = actor
  action.object_state_check!(*owners)
  'allowed'
rescue AccessDenied => e
  e.message
rescue NoMethodError => e
  raise unless e.name == :role && e.receiver.nil?

  'NoMethodError: nil.role'
end

def check(label, actual, expected)
  raise "#{label}: expected #{expected.inspect}, got #{actual.inspect}" unless actual == expected

  puts "PASS #{label}: #{actual}"
end

original = build_action(source, source_path)
proposed = build_action(source.sub(original_guard, proposed_guard), source_path)
actors = { anonymous: nil, user: Actor.new(:user), support: Actor.new(:support), admin: Actor.new(:admin) }
states = %w[active suspended soft_delete hard_delete deleted]

states.each do |state|
  owner = Owner.new(state, State.new('Synthetic account restriction'))
  actors.each do |role, actor|
    expected = if role == :admin || state == 'active'
                 'allowed'
               else
                 'Access forbidden: Synthetic account restriction'
               end

    check("original / #{role} / #{state}", result(original, actor, owner),
          role == :anonymous ? 'NoMethodError: nil.role' : expected)
    check("proposed / #{role} / #{state}", result(proposed, actor, owner), expected)
  end
end

[nil, ''].each do |reason|
  check("proposed / anonymous / suspended / reason=#{reason.inspect}",
        result(proposed, nil, Owner.new('suspended', State.new(reason))),
        'Access forbidden: your account is suspended')
end

check('proposed / anonymous / multiple owners',
      result(proposed, nil, Owner.new('active'), Owner.new('suspended', State.new('Synthetic restriction'))),
      'Access forbidden: Synthetic restriction')

puts '43 assertions passed; real helper loaded from the deployed revision, proposed change applied only in memory.'
