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
      name: _email.value.substring(0, _email.value.indexOf('@')),
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
  let _password = document.getElementById("userInfoPassword");
  let _name = document.getElementById("userInfoName");
  let _home_address = document.getElementById("userInfoAddress");
  fetch("/api/users/" + _username, {
    method: "PUT",
    body: JSON.stringify({
      password: _password.value,
      name: _name.value,
      home_address: _home_address.value,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
  .then(location.reload())
}

function create_creditcard(_id) {
  let _creditcard = document.getElementById("userAddCardNumber");
  fetch("/api/creditcard/" + _id, {
    method: "POST",
    body: JSON.stringify({
      card_number: _creditcard.value,
      owner_id: _id,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
  .then(location.reload());
}

function update_user_cc(_id) {
  let _creditcard = document.getElementById("userUpdateCardNumber");
  fetch("/api/creditcard/" + _id, {
    method: "PUT",
    body: JSON.stringify({
      card_number: _creditcard.value,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(location.reload());
}

function create_wishlist(user_id) {
  let _wishlist = document.getElementById("newWishlist");
  fetch("/api/wishlist/" + user_id, {
    method: "POST",
    body: JSON.stringify({
      name: _wishlist.value,
      owner_id: user_id,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  }).then(location.reload());
}

function delete_wishlist(wishlist_id) {
  fetch("/api/wishlist/" + wishlist_id, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  }).then(location.reload());
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

function delete_wishitem(wishitem_id) {
  fetch("/api/wishlist/wishitems/" + wishitem_id, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  }).then(location.reload());
}