# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'A CPA Ad Set',
  'campaign_id': '<adCampaignLinkClicksID>',
  'daily_budget': '5000',
  'start_time': '2024-04-08T11:26:05-0700',
  'end_time': '2024-04-15T11:26:05-0700',
  'billing_event': 'IMPRESSIONS',
  'optimization_goal': 'REACH',
  'bid_amount': '1000',
  'promoted_object': {'page_id':'<pageID>'},
  'targeting': {'facebook_positions':['feed'],'geo_locations':{'countries':['US']}},
  'user_os': 'iOS',
  'publisher_platforms': 'facebook',
  'device_platforms': 'mobile',
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)