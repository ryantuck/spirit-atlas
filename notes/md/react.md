# React

Learning react via repl.it. Remarkable how nice it is to get set up with no local dev.

https://repl.it/@ryantuck/react-boy#src/index.js

Really nice that imports happen very similar to python.

JSX = javascript with html tags. No excessive quoting, etc.

Classes need `render()`ing, but functions don't.

Can include different components in other components.

Props: can pass down props from parent to children.

Official react tutorial is good https://reactjs.org/tutorial/tutorial.html#what-is-react

Not sure why I can just use `{() => alert('hey')}` and don't need `{function() {alert('hey');}}`, but that's cool.

Keeping state in parent components is the normal pattern, as opposed to children holding their states.

Can use function components and pass in props instead of creating classes. Cleaner implementation. Note that these only work when the component doesn't need to manage its own state, so doesn't apply to parent classes (that are managing state)!

"React updates a component based on two conditions: If either the components props change or the state is updated using the this.setState function."


---

Additional bits:

- [react-markdown](https://rexxars.github.io/react-markdown/) renders md on the fly - could be really interesting for creating a web-based [[zettelkasten]]
