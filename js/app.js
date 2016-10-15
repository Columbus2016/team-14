var app = angular.module("FoodModule", ["ngRoute"]);
app.config(function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl: 'views/login.html',
        controller: 'LoginController'
    })
    .when('/dashboard', {
        templateUrl: 'views/dashboard.html'
        })
    .when('/profile', {
        templateUrl: 'views/profile.html',
        controller: 'ProfileController'
    })
    .when('/groups', {
        templateUrl: 'views/groups.html',
        controller: 'GroupController'
    })
    .when('/challenges', {
        templateUrl: 'views/challenges.html',
        controller: 'ProductController'
    })
    .otherwise({
        redirectTo: '/'
    });
});