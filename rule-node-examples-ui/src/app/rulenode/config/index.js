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


import filterComponents from './components/filter';
import enrichmentComponents from './components/enrichment';
import transformComponents from './components/transform';
import googleComponents from './components/google';
import CustomRuleNodeCoreConfig from './custom-nodes-config';

import ruleNodesTypes from './custom-nodes-types.constant';

export default angular.module('thingsboard.ruleChain.config',
    [ruleNodesTypes, filterComponents, enrichmentComponents, transformComponents, googleComponents])
    .config(CustomRuleNodeCoreConfig)
    .name;
