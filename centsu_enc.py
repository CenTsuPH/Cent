import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))
