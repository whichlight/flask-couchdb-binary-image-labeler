/*
 *Collect images from instagram through twitter
 *stdout prints the image urls
 */

var $ = require('jQuery');

var tweets = [];
var search_url = 'http://search.twitter.com/search.json'
var refresh_url = '?q=instagr.am&rpp=5&include_entities=true&result_type=recent'

var pullMoreImages = function(){
$.getJSON(search_url+refresh_url+'&callback=?',function(data){

	refresh_url = data.refresh_url;
	tweets.push.apply(tweets,data.results);
	$.each(data.results,function(index,d){
		url = d.entities.urls[0].expanded_url;
		var req_url = encodeURIComponent(url);
		src= url+"media/?size=l";	
		//write to stdout
		console.log(src);
		//write to stderr for monitoring
		process.stderr.write(src + '\n')	
	});	
});


}

setInterval(pullMoreImages,5000);
