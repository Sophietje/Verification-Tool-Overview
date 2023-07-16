const documents = [
  {
    id: 1,
    title: 'VerCors',
    text: "deductive verification java c reasoning memory safety functional correctness"
  },
  {
    id: 2, 
    title: 'verifast',
    text: "deductive verification java c c++ memory safety"
  },
  {
    id: 3,
    title: 'z3',
    text: "SMT solver solving satifiability modulo theories cvc4"
  }
]

const miniSearch = new MiniSearch({
  fields: ['title', 'text'], // fields indexed for search
  storeFields: ['title'], // fields returned with results
});

await miniSearch.addAllAsync(documents);

(async () => {
  const search = query => {
    const container = document.getElementById('results');
    if (query.length > 1) {
      const results = miniSearch.search(query, { boost: { title: 3 }, prefix: true, fuzzy: 0.3 });
      if (results.length == 0) {
        const noResults = document.createTextNode('No results found');
        container.replaceChildren(noResults);
      } else {
        const list = document.createElement('ul');
        results.slice(0, 10).forEach(result => {
          const item = document.createElement('li');
          const link = document.createElement('a');
          // link.setAttribute('href', result.pathname);
          link.appendChild(document.createTextNode(result.title));
          item.appendChild(link);
          list.append(item);
        });
        container.replaceChildren(list);
      }
    } else {
      //container.parentNode?.removeChild(container);
    }
  };

  input.addEventListener('input', event => {
    search(event.target.value);
  });
})();