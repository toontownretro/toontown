"""
Constants file that contains XML and misc. codes for award responses
"""

# --- Begin XML message constants ---


setLatestListFailureXML = """
<setLatestListResponse>
 <success>false</success>
 <error>%s</error>
</setLatestListResponse>
\r\n"""

setLatestListSuccessXML = """
<setLatestListResponse>
 <success>true</success>
 <info>%s</info>
</setLatestListResponse>
\r\n"""
