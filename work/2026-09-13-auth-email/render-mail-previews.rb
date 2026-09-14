# Render synthetic verification messages without loading an application database.
require 'active_support/all'
require 'erb'
require 'cgi'
require 'fileutils'

module VpsAdmin
  module API
  end
end

api_repo, production_repo, output_dir = ARGV
require File.join(api_repo, 'api/lib/vpsadmin/api/time_zones')

class PreviewContext
  def initialize
    @user = Struct.new(:login).new('example-member')
    @code = '012345'
    @requested_at = Time.utc(2026, 9, 14, 12)
    @expires_at = @requested_at + 1800
    @service_name = 'vpsAdmin WebUI'
    @device = 'Linux, Firefox 128.0 (Other)'
    @ip_address = '192.0.2.90'
    @ip_ptr = 'client.example.test'
    @support_mail = 'support@example.test'
  end

  def local_time(value, format = VpsAdmin::API::TimeZones::DEFAULT_TIME_FORMAT)
    VpsAdmin::API::TimeZones.format_time(value, time_zone: 'Europe/Prague', format:)
  end

  def render(source)
    ERB.new(source, trim_mode: '-').result(binding)
  end
end

roots = {
  'builtin' => File.join(api_repo, 'api/notification_templates/templates'),
  'vpsfree' => File.join(production_repo, 'templates')
}
FileUtils.mkdir_p(output_dir)
roots.each do |name, root|
  %w[cs en].each do |language|
    context = PreviewContext.new
    rendered = %w[text html].to_h do |format|
      source = File.read(File.join(root, 'user_login_email_verification/email', "#{language}.#{format}.erb"))
      [format, context.render(source)]
    end
    visible_html = CGI.unescapeHTML(rendered.fetch('html').gsub(/<style>.*?<\/style>/m, '').gsub(/<[^>]*>/, ' '))
    normalize = ->(text) { text.gsub(/\s+/, ' ').strip }
    raise "Content differs: #{name}/#{language}" unless normalize.call(visible_html) == normalize.call(rendered.fetch('text'))
    rendered.each do |format, content|
      extension = format == 'text' ? 'txt' : 'html'
      File.write(File.join(output_dir, "#{name}-#{language}.#{extension}"), content)
    end
    puts "Rendered #{name}/#{language}: plain text and HTML content match"
  end
end
