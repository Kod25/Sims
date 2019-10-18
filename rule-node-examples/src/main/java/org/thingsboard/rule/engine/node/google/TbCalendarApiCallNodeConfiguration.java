/**
 * Copyright © 2018 The Thingsboard Authors
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
package org.thingsboard.rule.engine.node.google;

import lombok.Data;
import org.thingsboard.rule.engine.api.NodeConfiguration;


@Data
public class TbCalendarApiCallNodeConfiguration implements NodeConfiguration<TbCalendarApiCallNodeConfiguration>{

    private String calendarId;
    private String requestMethod;
    private String serviceAccountKey;
    private String serviceAccountKeyFileName;

    @Override
    public TbCalendarApiCallNodeConfiguration defaultConfiguration() {
        TbCalendarApiCallNodeConfiguration configuration = new TbCalendarApiCallNodeConfiguration();
        configuration.setCalendarId("Calendar Id");
        configuration.setRequestMethod("GET");
        return configuration;
    }
}