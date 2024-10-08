response = [
  { body: 'Photo' }, // from uploadPhoto()
  { firstName: 'John', lastName: 'Doe' } // from createUser()
];

const [photo, user] = response;
console.log(photo);
console.log(user);
