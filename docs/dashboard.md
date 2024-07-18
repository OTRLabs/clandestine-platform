### Dashboard / UI:

#### UI Tech Stack

- [Vite](https://vitejs.dev/)
- [Litestar Vite Integration](https://github.com/cofin/litestar-vite)
- [Svelte](https://svelte.dev/)
- [Jinja2 Templates](https://docs.litestar.dev/2/reference/contrib/jinja.html)
- [Shadcn UI - Svelte Port](https://shadcn-svelte.com/)
- [Tor Hidden Services](https://tpo.pages.torproject.net/onion-services/portal/apps/web/)

### Requirements / Goals / Plans / Ideas

#### Limitations & Constraints
- We want to make an effort to make the `HTML views` as small as possible in size to deliver them effectively over `Tor`.

### Dashboard Description:

The `UI`/`dashboard` is designed to be lightweight in terms of size. The goal is to make the delivery of the `UI` when fetching `HTML`/`Svelte` components from the server a *fast* and *efficient* process.

We aim to design a dashboard-style system, where you are immediately directed to authenticate upon visiting the `root route` of the site.
We would like for there to be:
- a `vertical navigation bar` on the **left side** of the screen which focuses on `application functionality`, i.e., the features you came to the app for.
- positioned at the top left corner, there is a `horizontal navigation bar` with `drop-down menus`. These are more for `platform settings`, `application management`, `configs`, etc.

### Dashboard Design & Development

#### Real-Time Data
Real-time data should be pushed to the application via [Litestar Websockets](https://docs.litestar.dev/2/usage/websockets.html#websockets).

#### Dashboard Views
We will focus on building `views` using `Svelte` components served via the `Litestar` application. Using Vite for bundling and Svelte for creating reactive components will ensure a smooth and dynamic user experience.

#### Dashboard Reactivity

Using client-side scripting within this application is somewhat controversial among Tor users. While it introduces risks, we believe that the improved user experience provided by reactivity in web applications justifies its use.

To minimize risks, we will:
- Ensure minimal and secure JavaScript usage.
- Focus on Svelte's strengths in reactivity and component-based architecture.
- Use Litestar Websockets for real-time data, ensuring efficient and secure data handling.

#### Dashboard Components:

Our `Svelte` based `dashboard UI` will be very “component oriented”. 

The goal is to break each `view` down into individual sets of `Svelte components`. This will allow us to:
- Ensure each component gets the attention it needs for a polished, modern application feel.
- Implement best practices and standard behaviors (e.g., context menus on right-click).

Each component will be designed to:
- Be lightweight and efficient, reducing the overall size of the HTML views.
- Leverage Svelte’s reactivity to provide a dynamic user experience without extensive JavaScript.

### Example Migration Plan

1. **Identify Core Components**:
   - Identify key components or views that would benefit the most from Svelte’s reactivity and efficiency.
   - Start with those that are simpler to rewrite and have the most impact on user experience.

2. **Recreate Components in Svelte**:
   - Recreate these components using Svelte, leveraging its reactive features and component model.
   - Integrate Litestar Websockets for real-time updates within Svelte components.

3. **Test and Optimize**:
   - Test the Svelte components thoroughly to ensure they are performing well and the payload size is optimized.
   - Compare with the current HTMX implementation to quantify the improvements.



### Conclusion

By transitioning to Svelte and Vite, we aim to create a lightweight, efficient, and reactive dashboard UI that aligns with our goals of performance and user experience. This approach leverages the strengths of Svelte in building modern, component-based web applications while ensuring the overall system remains secure and performant for Tor users.