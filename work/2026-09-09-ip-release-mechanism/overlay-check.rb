# Run from vpsadmin/api with its spec environment. Uses only the disposable DB;
# notifications are built and inspected, never delivered to users.
require 'spec_helper'

RSpec.describe 'IP release notification overlay' do
  around { |example| with_current_context { example.run } }

  before do
    unlock_transaction_signer!
    ensure_available_node_status!(SpecSeed.node)
    ensure_user_mail_templates!
    SysConfig.find_or_initialize_by(category: 'webui', name: 'base_url').update!(value: 'https://vpsadmin.example.test')
    VpsAdmin::API::MailTemplates.reconcile!(
      path: File.join(ENV.fetch('IP_RELEASE_OVERLAY'), 'templates'),
      source_id: 'ip-release-reminder-review'
    )
  end

  %w[en cs].product(%w[requested reminder], [true, false], [[4], [6], [4, 6]]).each do |language, event, allow_keep, versions|
    it "renders #{language} #{event} with allow_keep=#{allow_keep}, IPv#{versions.join("/")}" do
      SpecSeed.user.update!(language: Language.find_by!(code: language))
      UserMailRoleRecipient.handle_update!(SpecSeed.user, 'admin', to: 'ip-notices@example.test')
      ips = versions.map do |version|
        network = version == 4 ? SpecSeed.network_v4 : SpecSeed.network_v6
        network.update!(primary_location: SpecSeed.location)
        create_ip_address!(network:, user: SpecSeed.user, addr: version == 4 ? '192.0.2.25' : '2001:db8::')
      end
      SpecSeed.location.update!(label: '<Prague & test>')
      campaign = IpReleaseCampaign.create_selected!(
        ids: ips.map(&:id), actor: SpecSeed.admin, label: 'Overlay runtime check',
        deadline: Time.utc(2030, 9, 16, 12), allow_keep:
      )
      campaign.notify!(event: 'requested', actor: SpecSeed.admin) if event == 'reminder'
      campaign.notify!(event:, actor: SpecSeed.admin)
      request = campaign.ip_release_requests.first
      mail = request.mail_log
      expect(mail.mail_template.template_id).to eq("ip_release_#{event}")
      expect(mail.mail_template.desc[:roles]).to eq([:admin])
      expect(mail.to).to eq('ip-notices@example.test')
      expect(mail.subject).not_to be_empty
      ips.each { |ip| expect(mail.text_plain).to include("#{ip.addr}/#{ip.prefix} (<Prague & test>)") }
      expect(mail.text_plain).to include("action=request&id=#{request.id}")
      expect(mail.text_html).to include('https://vpsadmin.example.test/?page=ip_release', '&lt;Prague &amp; test&gt;', "action=request&amp;id=#{request.id}")
      expect(mail.text_html).not_to include('<Prague')
      scarcity = language == 'en' ? 'Public IPv4 addresses are a scarce resource.' : 'Veřejných IPv4 adres je nedostatek.'
      [mail.text_plain, mail.text_html].each { |body| expect(body.include?(scarcity)).to eq(versions.include?(4)) }
      if language == 'en' && event == 'requested' && allow_keep && versions == [4]
        File.write(File.join(ENV.fetch('IP_RELEASE_PREVIEWS'), 'notice-en.html'), mail.text_html) if ENV['IP_RELEASE_PREVIEWS']
      elsif language == 'cs' && event == 'requested' && allow_keep && versions == [4]
        File.write(File.join(ENV.fetch('IP_RELEASE_PREVIEWS'), 'notice-cs.html'), mail.text_html) if ENV['IP_RELEASE_PREVIEWS']
      end
      expect(mail.text_plain).not_to include('<%', '%>')
      expect(mail.text_plain).to include(language == 'en' ? 'vpsFree.cz team' : 'tým vpsFree.cz')
      policy = if language == 'en'
                 allow_keep ? 'select it in vpsAdmin' : 'you can keep it by assigning it to a VPS.'
               else
                 allow_keep ? 've vpsAdminu ji vyber' : 'můžeš si ji ponechat přiřazením k VPS.'
               end
      expect(mail.text_plain.gsub(/\s+/, ' ')).to include(policy, '2030')
      expect(request.ip_release_request_notices.last.event).to eq(event)
    end
  end
end
