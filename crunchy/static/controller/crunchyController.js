var lifeExpectancyAnalysis = angular.module('lifeExpectancyAnalysis', []);

lifeExpectancyAnalysis.controller('lifeExpectancyController', ['$scope','$http',function ($scope,$http) {

$scope.data = {
    repeatSelect: null,
    availableOptions: [{'id': 'toffee' , 'name': 'toffee'}, {'id': 'tortilla','name': 'tortilla'},{'id': 'cracker' , 'name': 'cracker'}, {'id': 'biscotti' , 'name': 'biscotti' } , {'id': 'pickle' , 'name': 'pickle' } , {'id': 'radish' , 'name': 'radish' } , {'id': 'chips', 'name': 'chips'} , {'id': 'almond' , 'name': 'almond' } , {'id': 'celery' , 'name': 'celery'} , {'id': 'carrot', 'name': 'carrot'}, {'id': 'cereal' , 'name': 'cereal'}]
};

$scope.getGraphInfo = function ()
	{
		$http({
  			method: 'GET',
  			url: '/getDataForScatterPlot/' +  $scope.data.repeatSelect
			}).then(function successCallback(response) 
			{
				yAxisName = "";
				for(var i = 0; i < $scope.data.availableOptions.length; i++) 
				{
					if ( $scope.data.availableOptions[i]['id'] == $scope.data.repeatSelect )
					{
						yAxisName = $scope.data.availableOptions[i]['name']
					}
				}	
				 getGraph(response.data, yAxisName);
    			}, function errorCallback(response) {
                     });
	}

}]);
