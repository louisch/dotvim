" Theme
colorscheme molokai

" Logical size of GVim window
set lines=40 columns=105

" Don't display the toolbar
set guioptions-=T

" Font
if has('mac')
    set guifont=Monaco:h13
elseif has('unix')
    set guifont=Inconsolata\ Medium\ 12
endif

" If GUI is running call MiniBufExpl window
if has("gui_running")
    autocmd BufNew :call UMiniBufExplorer
endif
