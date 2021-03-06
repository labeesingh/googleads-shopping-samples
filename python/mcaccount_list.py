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

"""Gets all accounts on the specified multi-client account."""

import sys

from oauth2client import client
import shopping_common

# The maximum number of results to be returned in a page.
MAX_PAGE_SIZE = 50


def main(argv):
  # Authenticate and construct service.
  service, flags = shopping_common.init(argv, __doc__, __file__)
  merchant_id = flags.merchant_id

  try:
    request = service.accounts().list(
        merchantId=merchant_id, maxResults=MAX_PAGE_SIZE)

    while request is not None:
      result = request.execute()
      if 'resources' in result:
        accounts = result['resources']
        for account in accounts:
          print ('Account "%s" with name "%s" was found.' %
                 (account['id'], account['name']))

        request = service.accounts().list_next(request, result)
      else:
        print 'No accounts were found.'
        break

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
