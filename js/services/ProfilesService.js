app.factory("ProfilesService", [function () {
    var object = {
        profiles: [
            {
                username: '2shobhitsriv6@gmail.com',
                password: 'password',
                points: 0,
                name: 'Shobhit Srivastava',
                current: false
            }, {
                username: 'shobhit@uga.edu',
                password: 'password',
                points: 10,
                name: 'Joe Stein',
                current: false
            }
        ]
    };
    return object;
}]);