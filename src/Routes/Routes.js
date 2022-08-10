const backendRoutes = {
  search: (query) => {
    console.log(query);
    return `/tweets/search/recent?query=${query}`;
  },
  spacesTitle: (query, scheduled) => {
    return `/spaces/search?query=${query}&state=${scheduled}`;
  },
  stream: () => {
    return "/tweets/search/stream/rules";
  }
};

export { backendRoutes };
