## @package GOPubmedGraph

from GOGraph import GOGraph

class GOPubmedGraph(GOGraph):
    ## Create a pubmed graph from a GOGraph
    # @param    gograph A GOGraph to base this graph off of
    # @param    XMLFileName The file containing GO definitions and Pubmed ID
    #                       information in the format of the OBO in XML
    def __init__(self, gograph, XMLFileName):

    ## Applies a weight to the graph
    def weight(self):

    ## Returns a GOGenePubmedGraph version of itself
    # @param    gogenegraph The GOGeneGraph that this graph is to be merged with
    def toGOGenePubmedGraph(self):
