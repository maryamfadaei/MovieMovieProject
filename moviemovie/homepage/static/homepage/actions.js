function find_showtimes_with_current_date(movie_name) {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    today = mm+'/'+dd+'/'+yyyy;
    window.open("http://www.cineplex.com/Showtimes/"+movie_name+"/nearby-theatres?Date="+today)
}

