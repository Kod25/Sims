import CalendarApiCallConfigDirective from './calendar-api-call-config-directive';

export default angular.module('thingsboard.ruleChain.config.google', [])
  .directive('tbGoogleNodeCalendarApiCallConfig', CalendarApiCallConfigDirective)
  .name;
