app.factory("ProductsService", [function () {
    var products = {
        things: [
            {
                name: "Cheerios",
                points: 10
            }, {
                name: "Popcorn",
                points: 15
            }, {
                name: "butter",
                points: 20
            }
        ]
    };
    return products;
}]);