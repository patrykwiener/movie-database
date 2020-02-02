function changeFavouritesButton(obj) {
    function change_button(old_class, new_class, text) {
        obj.classList.remove(old_class);
        obj.classList.add(new_class);
        obj.text = text;
    }

    var lightClass = 'btn-light';
    var warningClass = 'btn-warning';

    var text = null;
    if (obj.classList.contains(lightClass)) {
        text = 'Added to favourites';
        change_button(lightClass, warningClass, text);
    } else {
        text = 'Add to favourites';
        change_button(warningClass, lightClass, text);
    }
}

function addToFavourites(obj) {
    $.ajax({
        url: '../add-favourites/',
        type: "GET",
        data: {'imdb_id': obj.id}
    }).done(function (returned_data) {
        var response_data = JSON.parse(returned_data);
        if (response_data.hasOwnProperty("added_to_favourites")) {
            if (response_data["added_to_favourites"] === true) {
                changeFavouritesButton(obj);
            }
        }
    });
}
