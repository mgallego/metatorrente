var $keywords = '';

function searchInMetaTorrent(keywords) {

    $keywords = keywords;
    var url = 'popup.html#' + keywords;

    chrome.windows.create({ url: url});//, width: 1200, height: 660 });
}

function genericOnClick(info, tab) {
    searchInMetaTorrent(info.selectionText);
}

var contexts = ["selection"];
for (var i = 0; i < contexts.length; i++) {
    var context = contexts[i];
    var title = "Test '" + context + "' menu item";
    var id = chrome.contextMenus.create({"title": "Search selection in MetaTorrent", "contexts":[context],
					 "onclick": genericOnClick});
}


