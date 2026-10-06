# frozen_string_literal: true

# Readiness-review reproduction only. Run with the isolated test database.
require 'spec_helper'

RSpec.describe 'Legacy authentication token at the documented cutover' do
  let(:user) { SpecSeed.user }
  let(:operation) { VpsAdmin::API::Operations::Authentication::ResetPassword.new }
  let(:request) { build_request(ip: '192.0.2.43', user_agent: 'Legacy token review probe') }

  before do
    unlock_transaction_signer!
    ensure_user_mail_templates!
    ensure_available_node_status!(SpecSeed.node)
    user.update!(password_reset: true, lockout: false)
    user.update_columns(authentication_generation: 0)
    allow(operation).to receive(:resolve_password_change_ptr).and_return('client.example.test')
  end

  it 'reproduces acceptance of a legacy token after an old-writer password change' do
    token = create_auth_token!(user:, purpose: 'reset_password')
    token.update!(opts: {}) # Old Password#create_auth_token stores no generation.

    # Exact predecessor User#set_password has no generation or token callbacks.
    # Persist its resulting columns to represent the old api2 writer after the
    # additive migration, before that writer is stopped at the drain barrier.
    VpsAdmin::API::CryptoProviders.current do |name, provider|
      user.update_columns(
        password_version: name,
        password: provider.encrypt(user.login, 'intervening-password'),
        password_reset: false,
        lockout: false
      )
    end

    expect(token.reload.authentication_current?).to be(true)
    result = operation.run(token, 'replacement-password', request:)
    expect(result.user).to eq(user)
    expect(VpsAdmin::API::CryptoProviders::Bcrypt.matches?(
      user.reload.password, user.login, 'replacement-password'
    )).to be(true)
  end

  it 'rejects an otherwise equivalent token after a new-writer password change' do
    token = create_auth_token!(user:, purpose: 'reset_password')
    user.set_password('intervening-password')
    user.save!

    expect do
      operation.run(token, 'replacement-password', request:)
    end.to raise_error(VpsAdmin::API::Exceptions::AuthenticationError, 'invalid token')
  end
end
