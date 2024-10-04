// This module create a promise with handling error
export default function createUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
