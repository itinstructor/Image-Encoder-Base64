from base64 import b64decode
import tkinter as tk

small_icon_data = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MTYwRDcyOTEwQkFGMTFFRjgwMzBBODI2ODVEMUU5NTciIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MTYwRDcyOTIwQkFGMTFFRjgwMzBBODI2ODVEMUU5NTciPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDoxNjBENzI4RjBCQUYxMUVGODAzMEE4MjY4NUQxRTk1NyIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDoxNjBENzI5MDBCQUYxMUVGODAzMEE4MjY4NUQxRTk1NyIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PtelSeIAAAL4SURBVHjahJNfTBRnFMV/883M7s7sll1wgdUmiqHFP2g0NGrUGgppwAcjj4YaUrUGTcRom/BWn5ombdI+NPJgjMamPpiYVJtooqYNIBjiA5omFgOSlj9SWAQUWBB2lt2vl8VW2j74JZP5Jrn3nHPPmWvwn1OwnV0rKziWCVExP8UqXxjDWcGw10/rSDPnxzppX15v/H2xggTWHeZrf5RjEz34y9fUUL17P06+wc/3b3Cr8zqx9/ASvVx4cpnGVIKXi33mq2ZnSyM/mQEODndifdVwlvpDx3kYb2WoZ4JPqj5lw+rNXL100yzYxjZ5do494MeMRyrLvukU35U2oHN3oOvO7NWDQwN6y5E8Ha5AO1vRG2vDenCkTx/5Yr/O/xBd9jl600nOLfaqaBk7gqs4Mf27fLhQubWGO79d4enQc0KiL28FjIxNca3lB6p31YhcEB8IraZe/HpfvV3FyblxTJGPKQCRaIjpyQTaE0BHKPyQnoN5I4FrhcQEwZC6F90YYnaD5caoHL0HegEy04rHfb8ynojzluPgSqGYhSEgA388FSQTN6zQOkPyuajbzAeWGLFydljYI1C67l1qq+ux/IrGj77MsimRvKhuIZ0iNZ/hl46bPOrtIhjJRlhoKVtU5sLMBPiKfKyNlbwOOY//HTcngBMTxRJiJi0EAhBfZLFkXsPWvOmk5jKkpqVWDDZ9PFMzg7RENoItkrSn3giglCKdFLVhmP2Tu9ZwM03FtRzIzKM8c4ZHIx14k+AJix2UQhlDi9SkjCjekZQ0lAgNvwP912lSkmlHoo9zkfUCn1YEAi42Ln7DxQm6BENylx/E1q6k4pIcV0R3CtALLo7epy27C3YObulpbkTsaOVu+2P8Mk4gX7IX1oXZpY1xC5fet7svM2U8a+v6ln2iMvHPMvlyCBbX8Y2viKOT3ViiipQ0m/4lw5yC7N+Xtj0u9X7PZ94UiX9t47J1Lo/toT5cQvnCHDFx3DAs4tLQFm/n/GgHLcvr/xJgACMXBrYILarSAAAAAElFTkSuQmCC"
large_icon_data = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MDk0MjYwQjYwQkFGMTFFRkJDNzBGOTcxNTVCMzY5MjQiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MDk0MjYwQjcwQkFGMTFFRkJDNzBGOTcxNTVCMzY5MjQiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDowOTQyNjBCNDBCQUYxMUVGQkM3MEY5NzE1NUIzNjkyNCIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDowOTQyNjBCNTBCQUYxMUVGQkM3MEY5NzE1NUIzNjkyNCIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PuEM94MAAAinSURBVHjapFdrUFTn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"
root = tk.Tk()
root.title("Window With Icon")
root.geometry("300x200")
small_icon = tk.PhotoImage(data=b64decode(small_icon_data))
root.iconphoto(False, small_icon)
root.mainloop()