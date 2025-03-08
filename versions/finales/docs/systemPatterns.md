# System Patterns: Livre 3 - Les Aventures d'Olivia et Martin

**System Architecture:**

The book project follows a simple structure:

*   **livre[N]/chapitres/:** Contains chapter drafts in Markdown format.
*   **livre[N]/illustrations/:** Contains illustration briefs, assets, and processed illustrations.
*   **livre[N]/docs/:** Contains project documentation, notes, and planning documents.
*   **common/:** Contains assets and documentation common to all books in the series.

**Key Technical Decisions:**

*   Markdown is used for chapter drafts for ease of writing and version control.
*   Illustrations are managed in separate folders with briefs and processed files.
*   Documentation is kept alongside the book content for easy access.

**Design Patterns:**

*   **Modular Chapter Structure:** Each chapter is a separate Markdown file, making it easy to edit and organize.
*   **Asset Organization:** Illustrations and common assets are organized in dedicated folders for clarity and reuse.

**Component Relationships:**

*   Chapters and illustrations are linked through briefs and filenames.
*   Documentation provides context and guidance for writing and illustration.
*   Common assets are used across all books in the series to maintain consistency.