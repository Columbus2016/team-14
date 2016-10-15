app.controller("LoginController", ['$scope', "ProfilesService", function($scope, ProfilesService) {
    $scope.profiles = ProfilesService.profiles;
    $scope.login = function() {
        var eUsername = document.getElementById("username").value;
        var ePassword = document.getElementById("password").value;
        if (eUsername == '2shobhitsriv6@gmail.com') {
            if (ePassword == 'password') {
                window.location.href = '#/dashboard';
                return;
            }
        }
        alert("Incorrect credentials.");
    };
}]);