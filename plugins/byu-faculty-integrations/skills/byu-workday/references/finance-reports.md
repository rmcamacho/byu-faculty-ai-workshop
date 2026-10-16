# Workday Finance Reports

## Finding the Right Report

BYU Financial Services sends faculty periodic emails that name and link the reports for the worktags they are responsible for. Prefer the report named there. At the time this skill was written, a high-level balance view was **BYU Budget Vs Actuals Overview by Driver Worktag**; confirm the current name with Workday search, because report names and layouts change.

## Running a Report

1. Open the report from search results labeled as a report, or from the user's link.
2. If a parameter dialog appears, read every prompt, default value, and checkbox filter. Show them to the user.
3. Change nothing unless the user specifies the exact new value. Do not save the parameters as defaults.
4. After the user confirms the parameters, a task script may run the report with `--apply` by pressing only the dialog's OK or Run control. This is the one permitted Workday apply action, because it reads data without changing a record.
5. Verify the result heading matches the requested report before reading rows.

## Reading the Result

Record and report each time:

- the report title, period, and run time;
- every active filter and exclusion, such as hiding closed or inactive worktags;
- the column headings exactly as shown;
- each worktag's ID, name, and type as displayed.

## Interpretation Rules

- **A filtered view is not a complete list.** Exclusions mean other worktags may exist. Never describe the rows as all of the user's accounts.
- **The Total row is not an account.** Do not add it to the sum or describe it as money available.
- **Balance is not spendability.** A remaining amount on a sponsored award is limited by its end date, budget categories, and allowability. Gift and startup funds may carry purpose restrictions.
- **Auxiliary or service-center worktags** may show budget variance rather than cash on hand. Say so instead of treating the figure as spendable.
- **Encumbrances** are committed but unpaid amounts, such as open purchase orders. Show whether a balance already subtracts them, based on the column definitions shown.
- **Negative balances** indicate overspending or timing differences; flag them for the research administrator rather than explaining them away.
- Copy numbers exactly as displayed. Do not infer currency, rounding, or fiscal period from formatting alone.
- Discover account IDs and periods from fresh output each time; never reuse figures from an earlier session as current.

## Answering Spending Questions

For "Can I buy X on account Y?", answer with what the report shows and what must still be confirmed: remaining amount after encumbrances, award end date, whether the item fits the sponsor budget and allowability rules, required approvals or quotes, and the BYU purchasing process. Point to the official BYU purchasing and expense pages for current policy rather than quoting thresholds from memory:

- https://purchasing.byu.edu/training
- https://purchasing.byu.edu/expense-reports-and-reimbursement
- https://purchasing.byu.edu/encumbrances
