from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:
    """
    Splits documents into smaller chunks.
    """

    @staticmethod
    def split_documents(documents):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
        )

        return splitter.split_documents(documents)