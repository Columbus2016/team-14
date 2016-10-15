app.controller("LogoutController", ["$scope", "ProfilesService", function($scope, ProfilesService) {
    $scope.profiles = ProfilesService.profiles;
    $scope.logout = function() {
        for (i = 0; i < $scope.profiles.length; i++) {
            if ($scope.profiles[i].current == true) {
                $scope.profiles[i].current = false;
                window.location.href = '#/';
                return;
            }
        }
    }
}]);