#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Gets all datafeeds on the specified account."""

import sys

from oauth2client import client
import shopping_common


def main(argv):
  # Authenticate and construct service.
  service, flags = shopping_common.init(argv, __doc__, __file__)
  merchant_id = flags.merchant_id

  try:
    request = service.datafeeds().list(merchantId=merchant_id)

    result = request.execute()
    if 'resources' in result:
      datafeeds = result['resources']
      for datafeed in datafeeds:
        print ('Datafeed "%s" with name "%s" was found.' %
               (datafeed['id'], datafeed['name']))
    else:
      print 'No datafeeds were found.'

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
