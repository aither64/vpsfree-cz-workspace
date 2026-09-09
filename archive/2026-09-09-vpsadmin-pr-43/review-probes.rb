# frozen_string_literal: true
# Run from the API Nix shell with bundle exec rspec /absolute/path/to/this/file.
require File.join(ENV.fetch('VPSADMIN_REPO_ROOT'), 'api/spec/api/plugins/payments/user_payment_spec')

payment_specs = RSpec.world.example_groups.find do |group|
  group.description == 'VpsAdmin::API::Resources::UserPayment'
end

payment_specs.class_exec do
  describe 'PR 43 review probes' do
    it 'paginates tied timestamps and includes without gaps or repeats' do
      timestamp = Time.utc(2026, 1, 15, 10, 30)
      rows = Array.new(5) { build_user_payment_at(user:, created_at: timestamp) }
      ids = []
      params = { limit: 2, created_from: timestamp.iso8601, created_to: timestamp.iso8601 }
      4.times do
        as(admin) { json_get index_path, user_payment: params, _meta: { includes: 'user,accounted_by' } }
        expect_status(200)
        user_payments.each { |row| expect(row.dig('user', '_meta', 'resolved')).to be(true) }
        page_ids = user_payments.map { |row| row.fetch('id').to_i }
        ids.concat(page_ids)
        break if page_ids.empty?

        params[:from_id] = page_ids.last
      end
      expect(ids).to eq(rows.reverse.map(&:id))
    end

    it 'converts timezone offsets on an inclusive singleton period' do
      selected = build_user_payment_at(user:, created_at: Time.utc(2026, 1, 15, 10, 30))
      build_user_payment_at(user:, created_at: Time.utc(2026, 1, 15, 11, 30))
      as(admin) do
        json_get index_path, user_payment: {
          created_from: '2026-01-15T11:30:00+01:00',
          created_to: '2026-01-15T11:30:00+01:00'
        }
      end
      expect_status(200)
      expect(user_payments.map { |row| row.fetch('id').to_i }).to eq([selected.id])
    end

    it 'accepts each date bound independently' do
      older = build_user_payment_at(user:, created_at: Time.utc(2026, 1, 1))
      newer = build_user_payment_at(user:, created_at: Time.utc(2026, 2, 1))
      as(admin) { json_get index_path, user_payment: { created_from: '2026-02-01T00:00:00Z' } }
      expect_status(200)
      expect(user_payments.map { |row| row.fetch('id').to_i }).to eq([newer.id])
      as(admin) { json_get index_path, user_payment: { created_to: '2026-01-01T00:00:00Z' } }
      expect_status(200)
      expect(user_payments.map { |row| row.fetch('id').to_i }).to eq([older.id])
    end

    it 'keeps total_count scoped to the period on subsequent pages' do
      older = build_user_payment_at(user:, created_at: Time.utc(2026, 1, 1))
      newer = build_user_payment_at(user:, created_at: Time.utc(2026, 2, 1))
      build_user_payment_at(user:, created_at: Time.utc(2025, 1, 1))
      as(admin) do
        json_get index_path, user_payment: {
          from_id: newer.id, limit: 1, created_from: '2026-01-01T00:00:00Z'
        }, _meta: { count: true }
      end
      expect_status(200)
      expect(user_payments.map { |row| row.fetch('id').to_i }).to eq([older.id])
      expect(json.dig('response', '_meta', 'total_count')).to eq(2)
    end

    it 'does not use another users payment as a pagination cursor' do
      build_user_payment_at(user:, created_at: Time.utc(2026, 1, 1))
      foreign = build_user_payment_at(user: other_user, created_at: Time.utc(2026, 2, 1))
      as(user) { json_get index_path, user_payment: { from_id: foreign.id } }
      expect_status(200)
      expect(user_payments).to eq([])
    end

    it 'rejects invalid datetime input without server errors' do
      ['not-a-date', ['2026-01-01'], { bad: 'value' }].each do |value|
        as(admin) { json_get index_path, user_payment: { created_from: value } }
        expect_status(200)
        expect(json.fetch('status')).to be(false)
        expect(response_errors).to have_key('created_from')
      end
    end

    it 'returns an empty result for an inverted period' do
      build_user_payment_at(user:, created_at: Time.utc(2026, 1, 1))
      as(admin) do
        json_get index_path, user_payment: {
          created_from: '2026-02-01T00:00:00Z', created_to: '2026-01-01T00:00:00Z'
        }
      end
      expect_status(200)
      expect(user_payments).to eq([])
    end
  end
end
