export default function shuffled(input_string) {
    return input_string.split("").sort(function(){return 0.5-Math.random()}).join(", ")
}
