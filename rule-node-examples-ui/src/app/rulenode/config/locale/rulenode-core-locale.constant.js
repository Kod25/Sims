/*
 * Copyright © 2016-2018 The Thingsboard Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
export default function addRuleNodeCoreLocaleEnglish($translateProvider) {

    var en_US = {
        "tb": {
            "rulenode": {
                "msg-key": "Message key",
                "input-key": "Input key",
                "output-key": "Output key",
                "calander-api-url": "Calenar url",
                "calander-api-url-required": "Calendar url is required",
                "request-method": "Request method",
                "calendar-service-account-key": "Google Calendar service account key file",
                "calendar-service-account-key-required": "Google Calendar service account key file is required",
                "drop-file": "Drop a file or click to select a file to upload",
                "no-file": "No file selected"
            }
        }
    };

    $translateProvider.translations('en_US', en_US);

}
