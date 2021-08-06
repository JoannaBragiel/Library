$(document).ready(function(){

    $("#script_form").submit(function(){

        var search = $("#books").val();

        if(search == '')
        {
            alert("Please enter requested book");
        }

        else{
            var url = '';
            var img = '';
            var title = '';
            var author = '';

            $.get("https://www.googleapis.com/books/v1/volumes?q=" + search, function(response){

                for (i = 0; i < response.items.length; i++)
                {
                title=$('<h5>') + response.items[i].volumeInfo.title + '</h5>';

                author=$('<h5>') + response.items[i].volumeInfo.authors + '</h5>';

                title.appendTo("#result");

                author.appendTo("#result");
                }
            });
        }
    });

    return false;

});

//<div id="search">
//    <form id="script_form">
//        <input type="search" id="books">
//        <label for="search"></label>
//        <button>Search</button>
//    </form>
//</div>
//
//<div id="result">
//
//</div>