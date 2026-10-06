# frozen_string_literal: true

# Characterization of review findings; these assertions expose unsafe behavior.
require 'spec_helper'
require File.expand_path('spec/lib/vpsadmin/api/authentication/basic_spec.rb', Dir.pwd)
require File.expand_path('spec/api/routes/password_recovery_route_spec.rb', Dir.pwd)

basic_group = RSpec.world.example_groups.find do |group|
  group.described_class == VpsAdmin::API::Authentication::Basic
end
basic_group.it 'reproduces missing Basic hash-upgrade client snapshots', :review_probe do
  user.update_columns(
    password_version: 'md5',
    password: VpsAdmin::API::CryptoProviders::Md5.encrypt(user.login, 'secret')
  )
  expect do
    expect(provider.send(:find_user, request, user.login, 'secret')).to eq(user)
  end.to change(PasswordChangeLog, :count).by(1)

  event = PasswordChangeLog.order(:id).last
  expect(user.reload.password_version).to eq('bcrypt')
  expect(event.client_ip_addr).to be_nil
  expect(event.client_ip_ptr).to be_nil
  expect(event.user_agent_id).to be_nil
  expect(UserSession.current.client_ip_addr).to eq('198.51.100.70')
end

recovery_group = RSpec.world.example_groups.find do |group|
  group.described_class == VpsAdmin::API::Authentication::PasswordRecovery
end
recovery_group.it 'reproduces passkey begin failing on a256character browser header', :review_probe do
  user = create_user_with_totp
  user.webauthn_credentials.create!(
    label: 'Review passkey',
    external_id: Base64.strict_encode64('review-credential-id'),
    public_key: 'not-a-real-public-key',
    sign_count: 0
  )
  recovery, raw_token = create_recovery(user:)
  csrf = exchange_email_token(raw_token)
  header 'X-CSRF-Token', csrf
  header 'Content-Type', 'application/json'
  header 'User-Agent', 'Review browser'
  post '/oauth2/password-reset/verify/webauthn/begin', '{}'
  expect(last_response.status).to eq(200)
  expect(recovery.webauthn_challenges).not_to be_empty

  header 'User-Agent', 'A' * 256
  post '/oauth2/password-reset/verify/webauthn/begin', '{}'
  expect(last_response.status).to eq(422)
  expect(JSON.parse(last_response.body).fetch('status')).to be(false)
end

RSpec.describe 'MailLog public nullability description', :review_probe do
  it 'declares its now-nullable user association nonnullable in both responses' do
    expect(VpsAdmin::API::Resources::MailLog::Index.output[:user].nullable?).to be(false)
    expect(VpsAdmin::API::Resources::MailLog::Show.output[:user].nullable?).to be(false)
  end
end
