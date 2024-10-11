# hindi_quotes.js
Web-API for [hindi-quotes.vercel.app](https://hindi-quotes.vercel.app) an website with api which displays random hindi quote

## Example
```JavaScript
async function main() {
	const { HindiQuotes } = require("./hindi_quotes.js")
	const hindiQuotes = new HindiQuotes()
	const randomQuote = await hindiQuotes.getRandomQuote()
	console.log(randomQuote)
}

main()
```
