" Most is copied from http://amix.dk/vim/vimrc.html
" Edited for some of my own preferences, with some other tricks from around the 
" internet.

set nocompatible

filetype off
call pathogen#runtime_append_all_bundles()
call pathogen#helptags()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => General
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Sets how many lines of history VIM has to remember
set history=700

" Enable filetype plugin
filetype plugin on
filetype indent on

" Set to auto read when a file is changed from the outside
set autoread

" Sets the map leader key, used for custom keyboard shortcuts
let mapleader=','

" Saving shortcut
nmap <leader>w :w!<cr>

" Quickly edit/reload the vimrc/gvimrc files.
nmap <silent> <leader>ve :e $MYVIMRC<CR>
nmap <silent> <leader>vs :so $MYVIMRC<CR>
nmap <silent> <leader>ge :e $MYGVIMRC<CR>
nmap <silent> <leader>gs :so $MYGVIMRC<CR>

" When vimrc is edited, reload it
autocmd! bufwritepost vimrc source ~/.vimrc

" Turns modelines off
set modelines=0

" Set the formatoptions (See :help fo-table)
set formatoptions+=oqaw

" Open lines and exit
map <leader>o o<Esc>
map <leader>O O<Esc>

" Shortcut for closing windows
map <leader>x :close<cr>

" Shortcut for closing everything
map <leader>q :qa!<cr>

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => VIM user interface
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Set 7 lines to the curors - when moving vertical..
set so=999

set wildmenu "Turn on Wild Menu

set ruler "Always show current position
set relativenumber "Line numbers that count from the current line

set cmdheight=2 "The commandbar height

set hidden "Change buffer - without saving

" Set backspace config
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

set ignorecase "Ignore case when searching
set smartcase

set hlsearch "Highlight search things

set incsearch "Make search act like search in modern browsers
set nolazyredraw "Don't redraw while executing macros 

set magic "Set magic on, for regular expressions

set showmatch "Show matching bracets when text indicator is over them
set mat=2 "How many tenths of a second to blink

" No sound on errors
set noerrorbells
set novisualbell
set t_vb=
set tm=500

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Files, backups and undo
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Turn backup off, since most stuff is in SVN, git anyway...
set nobackup
set nowb
set noswapfile

"Persistent undo
try
    set undodir=~/.vim/undodir
    set undofile
catch
endtry

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Colors and Fonts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
syntax enable "Enable syntax highlight

set encoding=utf8
try
    lang en_GB
catch
endtry

set ffs+=unix,dos,mac "Default file types

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Text, tab and indent related
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set expandtab
set shiftwidth=4
set tabstop=4
set softtabstop=4
set smarttab

set lbr
set tw=79

set autoindent "Auto indent
set cindent "Cindent
set cinkeys+=0={,0=},0=),0=#
set wrap "Wrap lines 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Command mode related
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Maps semi-colon to the colon (for command mode)
nnoremap ; :

" Maps $c to expand to the edited file's directory
cno $c e <C-\>eCurrentFileDir("e")<cr>
cno $q <C-\>eDeleteTillSlash()<cr>

" Bash like keys for the command line
cnoremap <C-A> <Home>
cnoremap <C-E> <End>
cnoremap <C-K> <C-U>
cnoremap <C-P> <Up>
cnoremap <C-N> <Down>

" A mapping to save with sudo when you forget to use it.
cmap w!! %!sudo tee > /dev/null %

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Moving around, tabs and buffers
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Map space to / (search) and c-space to ? (backgwards search)
map <space> /
map <C-space> ?
map <silent> <leader><cr> :noh<cr>

" Smart way to move btw. windows
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

" Move between wrapped lines
nnoremap j gj
nnoremap k gk

" Mappings for tabs
map <leader>n :tabnew<cr>
map <leader><Tab> :tabnext<cr>
map <leader><s-Tab> :tabprevious<cr>
map <leader>k :tabclose!<cr>

" When pressing <leader>cd switch to the directory of the open buffer
map <leader>d :cd %:p:h<cr>

""""""""""""""""""""""""""""""
" => Statusline
""""""""""""""""""""""""""""""
" Always hide the statusline
set laststatus=2

" Format the statusline
" First part is the file name, including flags for paste-mode, read-only etc.
set statusline=\ %{HasPaste()}%F%m%r%h\ %w
              \\ \ CWD:\ %r%{CurDir()}%h
              \\ \ \ Line:\ %l/%L\:%c

function! CurDir()
    let curdir = substitute(getcwd(), '/Users/amir/', "~/", "g")
    return curdir
endfunction

function! HasPaste()
    if &paste
        return 'PASTE MODE  '
    else
        return ''
    endif
endfunction

""""""""""""""""""""""""""""""
" => Spelling section
""""""""""""""""""""""""""""""
" Toggle spelling on and off
nmap <silent> <leader>s :set spell!<cr>
" Set region to British English
set spelllang=en_gb

""""""""""""""""""""""""""""""
" => GUI section
""""""""""""""""""""""""""""""
" Some GUI specific stuff.
if has("gui_running")
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
endif

""""""""""""""""""""""""""""""
" => Python section
""""""""""""""""""""""""""""""
let python_highlight_all = 1
au FileType python syn keyword pythonDecorator True None False self

au BufNewFile,BufRead *.jinja set syntax=htmljinja
au BufNewFile,BufRead *.mako set ft=mako

" If GUI is running call MiniBufExpl window
if has("gui_running")
    autocmd BufNew :call UMiniBufExplorer
endif

""""""""""""""""""""""""""""""
" => Minibuffer plugin
""""""""""""""""""""""""""""""
let g:miniBufExplModSelTarget = 1
let g:miniBufExplorerMoreThanOne = 1
let g:miniBufExplModSelTarget = 0
let g:miniBufExplUseSingleClick = 1
let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplVSplit = 18
let g:miniBufExplSplitBelow=1

let g:bufExplorerSortBy = "name"

map <leader>u :TMiniBufExplorer<cr>

""""""""""""""""""""""""""""""
" => MRU plugin
""""""""""""""""""""""""""""""
let MRU_Max_Entries = 400
map <leader>m :MRU<CR>

""""""""""""""""""""""""""""""
" => Command-T
""""""""""""""""""""""""""""""
let g:CommandTMaxHeight = 15
set wildignore+=*.o,*.obj,.git,*.pyc,wuala*

""""""""""""""""""""""""""""""


