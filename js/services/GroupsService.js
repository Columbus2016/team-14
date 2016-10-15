app.factory("GroupsService", [function () {
    var teams = {
        groups: [
            {
                name: "Georgia Tech",
                description: "The best damn school in the world.",
                points: 0,
                selected: true
            }, {
                name: "University of Georgia",
                description: "The worst damn school in the world.",
                points: 0,
                selected: false
            }
        ]
    };
    return teams;
}]);