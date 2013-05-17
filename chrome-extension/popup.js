var keywords = window.location.hash.substring(1);

function loadData(response) {
  var divloader = document.querySelector('#loader');
  divloader.style.display = "none";

    results = createResultTable(JSON.parse(response));
    $('#search-results').html(
	results
    );
}


function createResultTable(torrents) {
    
    if (torrents.length === 0) {
	return '<h2>Nothing found</h2>';
    };

    results = '<table class="table table-striped span12 table-hover"><thead><th>Title</th><th>Magnet</th><th>Size</th><th>Seed</th><th>Leech</th></thead>';
    
    for (i in torrents) {
	if (torrents[i].link != '') {
	    results = results + '<tr>';			  
	    results = results + '<td class="torrent-name"><a href="' + torrents[i].link +'" target="_blank">'
		+ torrents[i].name + '</a>  (' + torrents[i].site + ')</td>';
	    results = results + '<td class="magnet-link"><a href="' + torrents[i].magnet + '">Magnet</a></td>';
	    results = results + '<td class="size">' + torrents[i].size + '</td>';
	    results = results + '<td class="seed">' + torrents[i].seed + '</td>';
	    results = results + '<td class="leech">' + torrents[i].leech + '</td>';
	    results = results + '</tr>';			  
	}
    };
    results = results + "</table>";
    return results;
};


console.log("searching: " + keywords);
var req = new XMLHttpRequest();
req.open("GET", "http://metatorrent.herokuapp.com/api/torrents/" + keywords , true);
console.log(req);
req.onload = function (e) { 
    loadData(req.response);
};
req.send(null);




