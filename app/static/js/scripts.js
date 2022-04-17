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
