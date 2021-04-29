$('button.navbar_item_link').on('click', function(e) {
    e.preventDefault();
    $('.navbar_login').slideToggle('active');
});
$('.content').on('click', function(e) {
    $('.navbar_login').slideUp();
});


$('.rating_scientist_nav_list_link').on('click', function(e) {
    e.preventDefault();
    var way = $(this).attr('href');
    $('.rating_scientist_container.active').removeClass('active');
    $(way).addClass('active');
});
$('.rating_scientist_nav_list_item').on('click', function(e) {
    e.preventDefault();
    $('.rating_scientist_nav_list_item.active').removeClass('active');
    $(this).addClass('active');
});

$('.rating_scientist_nav_list_link_h').on('click', function(e) {
    e.preventDefault();
    var way = $(this).attr('href');
    $('.rating_scientist_container_h.active').removeClass('active');
    $(way).addClass('active');
});
$('.rating_scientist_nav_list_item_h').on('click', function(e) {
    e.preventDefault();
    $('.rating_scientist_nav_list_item_h.active').removeClass('active');
    $(this).addClass('active');
});

// $('.navbar_login.active .navbar_login_field').on('click', function() {
//     $('.navbar_login.active').show();
// });