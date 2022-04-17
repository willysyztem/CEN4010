function show_snackbar(msg) {
  Snackbar.show({ text: msg, pos: "bottom-center" });
}

function clear() {
  for (var i = 0; i < arguments.length; i++) {
    arguments[i].value = "";
  }
}

function register_user() {
  let _email = document.getElementById("email");
  let _password = document.getElementById("password");
  fetch("/api/users/", {
    method: "POST",
    body: JSON.stringify({
      email: _email.value,
      password: _password.value,
      name: _email.value.substring(0, _email.value.indexOf("@")),
      home_address: "Earth",
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(function (response) {
      if (!response.ok) {
        throw Error("Err: User Already Exist!");
      }
      console.log(response);
      show_snackbar("User Created Successfully!");
    })
    .catch(function (error) {
      console.log(error);
      show_snackbar(error);
    })
    .finally(function () {
      clear(_email, _password);
    });
}

function update_user(_username) {
  let _password = document.getElementById("userInfoPassword").value;
  let _name = document.getElementById("userInfoName").value;
  let _home_address = document.getElementById("userInfoAddress").value;
  fetch("/api/users/" + _username, {
    method: "PUT",
    body: JSON.stringify({
      password: _password,
      name: _name,
      home_address: _home_address,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function () {
    location.reload();
  });
}

function create_creditcard(_user_id) {
  let _creditcard = document.getElementById("userAddCardNumber").value;
  fetch("/api/creditcard/" + _user_id, {
    method: "POST",
    body: JSON.stringify({
      card_number: _creditcard,
      owner_id: _user_id,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function () {
    location.reload();
  });
}

function update_user_cc(_user_id) {
  let _creditcard = document.getElementById("userUpdateCardNumber").value;
  fetch("/api/creditcard/" + _user_id, {
    method: "PUT",
    body: JSON.stringify({
      card_number: _creditcard,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function () {
    location.reload();
  });
}

function create_wishlist(_user_id) {
  let _wishlist = document.getElementById("newWishlist").value;
  fetch("/api/wishlist/" + _user_id, {
    method: "POST",
    body: JSON.stringify({
      name: _wishlist,
      owner_id: _user_id,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function () {
    location.reload();
  });
}

function delete_wishlist(_wishlist_id) {
  fetch("/api/wishlist/" + _wishlist_id, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function () {
    location.reload();
  });
}

function add_wishitem(_wishlist_id, _book_id) {
  fetch("/api/wishlist/wishitems/", {
    method: "POST",
    body: JSON.stringify({
      wishlist_id: _wishlist_id,
      book_id: _book_id,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => show_snackbar(data.detail));
}

function delete_wishitem(_wishitem_id) {
  fetch("/api/wishlist/wishitems/" + _wishitem_id, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function () {
    location.reload();
  });
}

function add_cartitem(_user_id, _book_id) {
  fetch("/api/shoppingcart/cartitems/" + _user_id, {
    method: "POST",
    body: JSON.stringify({
      book_id: _book_id,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => show_snackbar(data.detail));
}

function delete_cartitem(_cartitem_id) {
  fetch("/api/shoppingcart/cartitems/" + _cartitem_id, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function () {
    location.reload();
  });
}

function add_wishitem_to_wishlist(_wishitem_id, _user_id) {
  fetch("/api/wishlist/wishitem/" + _wishitem_id + "&&" + _user_id, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function () {
    location.reload();
  });
}

function create_book() {
  let isbn = document.getElementById("book_isbn");
  let title = document.getElementById("book_title");
  let published_date = document.getElementById("book_published_date");
  let description = document.getElementById("book_description");
  let price = document.getElementById("book_price");
  let copies_sold = document.getElementById("book_copies");
  let author_id = document.getElementById("book_author");
  let publisher_id = document.getElementById("book_publisher");
  let genre = document.getElementById("book_genre");
  let pages = document.getElementById("book_pages");

  fetch("/api/books/", {
    method: "POST",
    body: JSON.stringify({
      isbn: isbn.value,
      title: title.value,
      published_date: published_date.value,
      description: description.value,
      price: price.value,
      copies_sold: copies_sold.value,
      author_id: author_id.value,
      publisher_id: publisher_id.value,
      genre: genre.value,
      pages: pages.value,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(function (response) {
      if (!response.ok) {
        throw Error("Err: Could Not Create Book");
      }
      console.log(response);
      show_snackbar("Book Created Successfully!");
    })
    .catch(function (error) {
      console.log(error);
      show_snackbar(error);
    })
    .finally(function () {
      clear(
        isbn,
        title,
        published_date,
        description,
        price,
        copies_sold,
        author_id,
        publisher_id,
        genre,
        pages
      );
    });
}

function create_author() {
  let author_first_name = document.getElementById("author_first_name");
  let author_last_name = document.getElementById("author_last_name");
  let author_biography = document.getElementById("author_biography");

  fetch("/api/authors/", {
    method: "POST",
    body: JSON.stringify({
      first_name: author_first_name.value,
      last_name: author_last_name.value,
      biography: author_biography.value
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(function (response) {
      if (!response.ok) {
        throw Error("Err: Could Not Create Author");
      }
      console.log(response);
      show_snackbar("Author Created Successfully!");
    })
    .catch(function (error) {
      console.log(error);
      show_snackbar(error);
    })
    .finally(function () {
      clear(author_first_name, author_last_name, author_biography);
    });
}

function create_author() {
  let author_first_name = document.getElementById("author_first_name");
  let author_last_name = document.getElementById("author_last_name");
  let author_biography = document.getElementById("author_biography");

  fetch("/api/authors/", {
    method: "POST",
    body: JSON.stringify({
      first_name: author_first_name.value,
      last_name: author_last_name.value,
      biography: author_biography.value
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(function (response) {
      if (!response.ok) {
        throw Error("Err: Could Not Create Publisher");
      }
      console.log(response);
      show_snackbar("Publisher Created Successfully!");
    })
    .catch(function (error) {
      console.log(error);
      show_snackbar(error);
    })
    .finally(function () {
      clear(author_first_name, author_last_name, author_biography);
    });
}

function create_publisher() {
  let publisher_name = document.getElementById("publisher_name");
  let publisher_country = document.getElementById("publisher_country");

  fetch("/api/publishers/", {
    method: "POST",
    body: JSON.stringify({
      company_name: publisher_name.value,
      country: publisher_country.value,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(function (response) {
      if (!response.ok) {
        throw Error("Err: Could Not Create Publisher");
      }
      console.log(response);
      show_snackbar("Publisher Created Successfully!");
    })
    .catch(function (error) {
      console.log(error);
      show_snackbar(error);
    })
    .finally(function () {
      clear(publisher_name, publisher_country);
    });
}