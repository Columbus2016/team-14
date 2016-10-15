app.controller("ProfileController", ['$scope', 'ProfilesService', function($scope, ProfilesService) {
    $scope.profiles = ProfilesService.profiles;
}]);