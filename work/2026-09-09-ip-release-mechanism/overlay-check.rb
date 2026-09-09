# Run from vpsadmin/api with its spec environment. Uses only the disposable DB;
# notifications are built and inspected, never delivered to users.
require 'spec_helper'

RSpec.describe 'IP release notification overlay' do
  around { |example| with_current_context { example.run } }

  before do
    unlock_transaction_signer!
    ensure_available_node_status!(SpecSeed.node)
    ensure_user_mail_templates!
    VpsAdmin::API::MailTemplates.reconcile!(
      path: File.join(ENV.fetch('IP_RELEASE_OVERLAY'), 'templates'),
      source_id: 'ip-release-runtime-review-420c98c'
    )
  end

  %w[en cs].product(%w[requested updated], [true, false]).each do |language, event, allow_keep|
    it "renders #{language} #{event} with allow_keep=#{allow_keep}" do
      SpecSeed.user.update!(language: Language.find_by!(code: language))
      ip = create_ip_address!(user: SpecSeed.user)
      campaign = IpReleaseCampaign.create_selected!(
        ids: [ip.id], actor: SpecSeed.admin, label: 'Overlay runtime check',
        deadline: Time.utc(2030, 9, 16, 12), allow_keep:
      )
      campaign.notify!(event:, actor: SpecSeed.admin)
      request = campaign.ip_release_requests.first
      mail = request.mail_log
      expect(mail.subject).not_to be_empty
      expect(mail.text_plain).to include("#{ip.addr}/#{ip.prefix}", "action=request&id=#{request.id}")
      expect(mail.text_plain).not_to include('<%', '%>')
      expect(mail.text_plain).to include(language == 'en' ? 'vpsFree.cz team' : 'tým vpsFree.cz')
      policy = if language == 'en'
                 allow_keep ? 'entering a reason in vpsAdmin' : 'Previously submitted reasons do not prevent release'
               else
                 allow_keep ? 'po zadání důvodu ve vpsAdminu' : 'Dříve zadané důvody podle aktuálních pravidel'
               end
      expect(mail.text_plain).to include(policy, '2030')
      expect(request.ip_release_request_notices.last.event).to eq(event)
    end
  end
end
