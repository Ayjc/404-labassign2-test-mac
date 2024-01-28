import { Picker } from "emoji-mart"; // import Picker class from module
// This is where you would import other modules you installed with npm too, but for this example we only have the emoji-mart.

const pickerOptions = { onEmojiSelect: console.log }
const picker = new Picker(pickerOptions) // instantiate object
document.body.appendChild(picker) // add to DOM
