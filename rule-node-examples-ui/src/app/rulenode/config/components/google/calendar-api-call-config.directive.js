import calendarApiCallConfigTemplate from './calendar-api-call-config-tpl.html';

export default function CalendarApiCallConfigDirective($compile){
  var linker = function(scope, element, attrs, ngModelCtrl){
    var template = calendarApiCallConfigTemplate;
    element.html(template);

    scope.$watch('configuraton', function(newConfiguration, oldConfiguration){
      if(!angular.equals(newConfiguration, oldConfiguration)){
        ngModelCtrl.$setViewValue(scope.configuration);
      }
    });
    ngModelCtrl.$render = function(){
      scope.configuraton = ngModelCtrl.$viewValue;
    };
    $compile(element.contents())(scope);
  };
  return{
    restrict: "E",
    require: "^ngModel",
    scope: {},
    link: linker
  };
}
