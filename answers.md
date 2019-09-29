# Technical Questions

#### 1. How long did you spend on the coding test below? What would you add to your solution if you had more time? If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add.

I have spend 6 days on this coding task. The delay was because of the following reasons.

 1. I chooses to do this task in **Python**, **Django** & **Vue**. As i am new to this tech stack i had to spend a lot of time in learning and figuring out things.
 2. I am currently a fulltime employee and had to do my daily job.

If i would have more time i would have improved the ranking logic. Currently when there is a new Favorite thing added with a rank that already exists for that given category i am just incrementing the ranks of all favorite things of that category where rank is >= incoming rank. An improved version of this logic will be as follows,
Assume these are the following ranks which are already in database

    [4, 5, 6, 9, 10, 15]

If there is an incoming rank with value **4** then the existing ranks should have been updated like this

    [5, 6, 7, 9, 10, 15] //4, 5, 6 gets incremented, 9, 10 & 15 remains same

This logic increments the existing rank until there is no gap between ranks. This way the `9, 10, 15` ranks will not get effected. Even with this logic there is a worst case scenario when there is no gap left between numbers. In that case we still have to increment all existing ranks. 

#### 2. What was the most useful feature that was added to the latest version of your chosen language? Please include a snippet of code that shows how you've used it.

In `ReactJS` i have used `React.lazy` and `Suspense` which is good for lazy loading of components and code splitting. This helps to reduce the bundle size which is loaded the first time user visits the website. Good for improving performance of the application.

    const SaveDraftModal = React.lazy(() => import('./modals/save_draft_modal.jsx'));
    
    <ErrorBoundary>
    	<React.Suspense  fallback={<ModalPlaceholder/>}>
    		<SaveDraftModal/>
    	</React.Suspense>
    </ErrorBoundary>

#### 3. How would you track down a performance issue in production? Have you ever had to do this?

Yes this is something which I have done quite often. Recently we encountered an issue with the production, the notification feed for users was not loading. We were using MongoDB so I checked the statistics of database instance. The CPU and RAM usage was high and there were lot of pending requests on the instance. I used MongoDB's `explain` query. During further debugging and examining `executionStats, queryPlanner` I found out that there were indexes missing on couple of notification feed collection's fields. In general the performance debugging includes (but not limited to):
1. Investigate how many database queries are being executed and try to reduce count of those
2. Investigate which queries are taking lot of time and optimize them e.g. using db indexes
3. Backend code optimization
