app.controller("ProductController",['$scope', "ProductsService", "GroupsService", "ProfilesService", function($scope, ProductsService, GroupsService, ProfilesService) {
    $scope.products = ProductsService.things;
    $scope.groups = GroupsService.groups;
    $scope.profiles = ProfilesService.profiles;
    $scope.buy = function(index) {
        console.log(index);
        var amount = $scope.products[index].points;
        for (i = 0; i < $scope.groups.length; i++) {
            if ($scope.groups[i].selected == true) {
                $scope.groups[i].points += amount;
                break;
            }
        }
        $scope.profiles[0].points += amount;
    }
}]);