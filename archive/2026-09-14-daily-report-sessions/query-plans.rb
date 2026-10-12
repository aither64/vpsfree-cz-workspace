require 'spec_helper'

now = Time.utc(2026, 9, 14, 12)
user_id = 900_000
sessions = Array.new(5_000) do |index|
  {
    user_id:,
    auth_type: 'token',
    api_ip_addr: '127.0.0.1',
    client_version: 'query-plan-fixture',
    created_at: now - ((index % 60) * 86_400) - 60,
    closed_at: index < 10 ? nil : now - 30
  }
end
UserSession.insert_all!(sessions)
PasswordChangeLog.insert_all!(sessions.map { |row| { user_id:, source: 'authenticated', created_at: row[:created_at] } })
UserFailedLogin.insert_all!(sessions.map do |row|
  { user_id:, auth_type: 'password', reason: 'invalid password', api_ip_addr: '127.0.0.1',
    client_version: 'query-plan-fixture', created_at: row[:created_at] }
end)
connection = ActiveRecord::Base.connection
%w[user_sessions password_change_logs user_failed_logins].each do |table|
  connection.execute("ANALYZE TABLE #{table}")
  relation = table.classify.constantize.where(created_at: (now - 86_400)...now)
  puts "#{table} period count"
  puts connection.select_all("EXPLAIN SELECT COUNT(*) FROM (#{relation.select(:id).to_sql}) AS report_rows").to_a.inspect
end
puts 'open session selection'
puts connection.select_all('EXPLAIN SELECT COUNT(*) FROM user_sessions WHERE closed_at IS NULL').to_a.inspect
puts 'actual active-session relation'
helper = VpsAdmin::API::DailyReportAuthentication.new(from: now - 86_400, to: now)
puts connection.select_all("EXPLAIN #{helper.send(:active_sessions).to_sql}").to_a.inspect
