app.controller("GroupController", ['$scope', "GroupsService", function($scope, GroupsService) {
    $scope.groups = GroupsService.groups;
}]);